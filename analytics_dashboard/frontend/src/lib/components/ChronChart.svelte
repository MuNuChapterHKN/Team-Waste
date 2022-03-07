<script lang="ts">
  import Chart from "$lib/components/Chart.svelte";
  import { cachedCubeLoad } from "$lib/utils/cachingCubeClient";
  import { cubeDataToLineData } from "$lib/utils";
  import type { Query } from "@cubejs-client/core";

  export let query: Query;
  export let colors: string[] | string;

  // TODO: Add button to change granularity from ui
  query.timeDimensions = query.timeDimensions.map((td) => {
    return { ...td, granularity: "day" };
  });
</script>

{#await cachedCubeLoad(query)}
  <p class="p-5">Loading...</p>
{:then data}
  <Chart data={cubeDataToLineData(data, query, colors)} type={"line"} />
{:catch err}
  <p class="text-red-500">Error message: {err}</p>
{/await}
