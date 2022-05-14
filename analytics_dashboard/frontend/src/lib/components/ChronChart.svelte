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
  import type { DateRange, Query } from "@cubejs-client/core";
  import type { ChartData } from "chart.js";
  import { onMount } from "svelte";
  import GranularitySelector from "./GranularitySelector.svelte";

  export let query: Query;
  // This component is not reactive on this prop
  const baseQuery = query;

  // State variable: ChartData shown in the chart
  let chartData: ChartData = null;

  // build a query with changed granularity
  const buildQuery = (granularity: Granularity) => {
    // const dateRange = {
    //   hour: "Today",
    //   day: "This month",
    // };
    const query = {
      ...baseQuery,
      limit: 48,
      timeDimensions: baseQuery.timeDimensions.map((td) => ({
        ...td,
        granularity,
        // dateRange: dateRange[granularity],
      })),
    };

    return query;
  };


  // Fetchs and transform the data based on a given granularity, then it updates the state variable
  const loadData = (granularity: Granularity) => {
    const query = buildQuery(granularity);
    cachedCubeLoad(query)
      .then((result) => {
        chartData = !!result
          ? cubeDataToLineData(result, granularity, $selectedColors)
          : null;
      })
      .catch(console.error);
  };

  // Loads the initial data when the component is mounted
  onMount(() => {
    loadData(Granularity.Day);
  });
</script>

{#if chartData == null}
  <p class="p-5">Loading...</p>
{:else}
  <GranularitySelector
    options={[Granularity.Day, Granularity.Hour]}
    on:change={evt => loadData(evt.detail)}
  />
  <Chart data={chartData} type={"line"} />
{/if}
