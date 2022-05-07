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
import GranularitySelector from "./GranularitySelector.svelte";

  export let query: Query;

  let granularity: Granularity = Granularity.Day;

  const handleClick = (evt) => {
    granularity =
      evt.detail;
  };

  // const dateRange = {
  //   hour: "Today",
  //   day: "This month",
  // };
  query.limit = 48;
  $: query.timeDimensions = query.timeDimensions.map((td) => {
    return {
      ...td,
      granularity,
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
  <GranularitySelector
    options={[Granularity.Day, Granularity.Hour]}
    on:change={handleClick}
  />
  <Chart {data} type={"line"} />
{/if}
