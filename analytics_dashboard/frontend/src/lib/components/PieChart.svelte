<script lang='ts'>
import { cachedCubeLoad } from "$lib/utils/cachingCubeClient";
import { cubeDataToPieData } from "$lib/utils/mappers";
import type { ChartData } from 'chart.js';

import type { Query, ResultSet } from "@cubejs-client/core";
import Chart from "./Chart.svelte";


    export let query: Query;
    export let colors: string[] | string;

    // let result: ResultSet|null = null;
    let data: ChartData = null;

    cachedCubeLoad(query)
        .then(result => data = cubeDataToPieData(result, colors))
        .catch(console.error);
</script>

{#if data == null}
  <p class="p-5">Loading...</p>
{:else}
  <Chart data={data} type={"pie"} />
{/if}