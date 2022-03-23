<script lang="ts">
  import Chart from "$lib/components/Chart.svelte";

  import { cachedCubeLoad } from "$lib/utils/cachingCubeClient";
  import { cubeDataToLineData } from "$lib/utils/mappers";
  import { writable } from "svelte/store";

  import type { Query, ResultSet } from "@cubejs-client/core";
  import type { Writable } from "svelte/store";

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

  const result: Writable<ResultSet|null> = writable(null);
  
  const loadData = (q: Query) => {
    cachedCubeLoad(q)
      .then(data => result.set(data));
  }

  $: loadData(query)
</script>


{#if $result == null}
  <p class="p-5">Loading...</p>
{:else}
  <button on:click={handleClick}>switch granularity</button>
  <Chart data={cubeDataToLineData($result, colors)} type={"line"} />
{/if}