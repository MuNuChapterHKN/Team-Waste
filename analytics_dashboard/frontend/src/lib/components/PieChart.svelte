<script lang='ts'>
import { cachedCubeLoad } from "$lib/utils/cachingCubeClient";
import { cubeDataToPieData } from "$lib/utils/mappers";

import type { Query, ResultSet } from "@cubejs-client/core";
import Chart from "./Chart.svelte";


    export let query: Query;
    export let colors: string[] | string;

    let result: ResultSet|null = null;

    cachedCubeLoad(query)
        .then(data => result = data)
        .catch(console.error);

    $: console.log(result?.series())
</script>

{#if result == null}
  <p class="p-5">Loading...</p>
{:else}
  <Chart data={cubeDataToPieData(result, colors)} type={"pie"} />
{/if}