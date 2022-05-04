<script lang="ts">
  import Chart from "$lib/components/Chart.svelte";
  import { cachedCubeLoad } from "$lib/utils/cachingCubeClient";
  import { selectedColors } from "$lib/utils/colors";
  import { cubeDataToLineData } from "$lib/utils/mappers";
  import type { Query, ResultSet } from "@cubejs-client/core";

  export let query: Query;

  let granularity: "day" | "hour" | "minute" | "second" = "day";

  const handleClick = () => {
    granularity = granularity == "day" ? "hour" : "day";
  };

  // TODO: limit number of datapoints
  $: query.timeDimensions = query.timeDimensions.map((td) => {
    return { ...td, granularity: granularity };
  });

  let fetched: ResultSet = null;

  const loadData = (q: Query) => {
    cachedCubeLoad(q)
      .then((result) => (fetched = result))
      .catch(console.error);
  };

  $: loadData(query);
  $: data =
    fetched === null ? null : cubeDataToLineData(fetched, $selectedColors);
</script>

{#if data == null}
  <p class="p-5">Loading...</p>
{:else}
  <button on:click={handleClick}>switch granularity</button>
  <Chart {data} type={"line"} />
{/if}
