<script lang="ts">
  import Chart from "$lib/components/Chart.svelte";
  import { cachedCubeLoad } from "$lib/utils/cachingCubeClient";
  import { cubeDataToLineData } from "$lib/utils/mappers";
  import type { Query, ResultSet } from "@cubejs-client/core";
  import type { ChartData } from "chart.js";

  export let query: Query;
  export let colors: string[] | string;

  let granularity: "day" | "hour" | "minute" | "second" = "day";

  const handleClick = () => {
    granularity = granularity == "day" ? "hour" : "day";
  };

  // TODO: limit number of datapoints
  $: query.timeDimensions = query.timeDimensions.map((td) => {
    return { ...td, granularity: granularity };
  });

  let data: ChartData = null;

  const loadData = (q: Query) => {
    cachedCubeLoad(q)
      .then((result) => (data = cubeDataToLineData(result, colors)))
      .catch(console.error);
  };

  $: loadData(query);
</script>

{#if data == null}
  <p class="p-5">Loading...</p>
{:else}
  <button on:click={handleClick}>switch granularity</button>
  <Chart {data} type={"line"} />
{/if}
