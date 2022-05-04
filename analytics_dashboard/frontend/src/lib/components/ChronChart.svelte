<script context="module" lang="ts">
  export enum Granularity {
    Day = "day",
    Hour = "hour",
    Minute = "minute",
    Second = "second",
  }
</script>

<script lang="ts">
  import Chart from "$lib/components/Chart.svelte";
  import { cachedCubeLoad } from "$lib/utils/cachingCubeClient";
  import { selectedColors } from "$lib/utils/colors";
  import { cubeDataToLineData } from "$lib/utils/mappers";
  import type { DateRange, Query, ResultSet } from "@cubejs-client/core";

  export let query: Query;

  let granularity: Granularity = Granularity.Day;

  const handleClick = () => {
    granularity =
      granularity === Granularity.Day ? Granularity.Hour : Granularity.Day;
  };

  // TODO: limit number of datapoints
  // const dateRange = {
  //   hour: "Today",
  //   day: "This month",
  // };
  $: query.timeDimensions = query.timeDimensions.map((td) => {
    return {
      ...td,
      granularity: granularity,
      // dateRange: dateRange[granularity],
    };
  });

  let fetched: ResultSet = null;

  const loadData = (q: Query) => {
    cachedCubeLoad(q)
      .then((result) => (fetched = result))
      .catch(console.error);
  };

  $: loadData(query);
  $: data =
    fetched === null
      ? null
      : cubeDataToLineData(fetched, granularity, $selectedColors);
</script>

{#if data == null}
  <p class="p-5">Loading...</p>
{:else}
  <button on:click={handleClick}>switch granularity</button>
  <Chart {data} type={"line"} />
{/if}
