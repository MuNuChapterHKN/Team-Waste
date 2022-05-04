<script lang="ts">
  import { cachedCubeLoad } from "$lib/utils/cachingCubeClient";
  import { cubeDataToPieData } from "$lib/utils/mappers";
  import type { Query, ResultSet } from "@cubejs-client/core";
  import Chart from "./Chart.svelte";
  import { selectedColors } from "$lib/utils/colors";

  export let query: Query;

  let fetched: ResultSet = null;

  cachedCubeLoad(query)
    .then((result) => (fetched = result))
    .catch(console.error);

  $: data =
    fetched === null ? null : cubeDataToPieData(fetched, $selectedColors);
</script>

{#if data == null}
  <p class="p-5">Loading...</p>
{:else}
  <Chart {data} type={"pie"} />
{/if}
