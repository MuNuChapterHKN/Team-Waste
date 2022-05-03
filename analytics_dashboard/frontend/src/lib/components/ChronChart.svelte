<script lang="ts">
  import Chart from "$lib/components/Chart.svelte";

  import { cachedCubeLoad } from "$lib/utils/cachingCubeClient";
  import { cubeDataToLineData } from "$lib/utils/mappers";

  import type { Query, ResultSet } from "@cubejs-client/core";

  export let query: Query;
  export let colors: string[] | string;

  let granularity: 'day'|'hour'|'minute'|'second' = 'day';

  const handleClick = () => {
    granularity = granularity == 'day' ? 'hour' : 'day';
  }

  // TODO: limit number of datapoints
  $: query.timeDimensions = query.timeDimensions.map((td) => {
    return { ...td, granularity: granularity };
  });

  let result: ResultSet|null = null;
  
  const loadData = (q: Query) => {
    cachedCubeLoad(q)
      .then(data => result = data)
      .catch(console.error);
  }

  $: loadData(query)
</script>


{#if result == null}
  <p class="p-5">Loading...</p>
{:else}
  <button on:click={handleClick}>switch granularity</button>
  <Chart data={cubeDataToLineData(result, colors)} type={"line"} />
{/if}
