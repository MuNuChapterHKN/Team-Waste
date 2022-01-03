<script lang='ts'>
import { cubeClient } from '$lib/stores';

import Chart, { ChartData, Title } from 'chart.js/auto';
import type { TimeQuery } from 'src/types/time_query.type';
import { onMount } from 'svelte';
import { colorSchema } from './colors';

export let query: TimeQuery;
if (query.colorScheme != null) {
    query.colors = colorSchema[query.colorScheme] 
}


// TODO: Get evenly spaced colors
function randomColor() {
    return '#'+(Math.random()*0xFFFFFF<<0).toString(16);
}

let chartElem;
let chart: Chart;


let loading = true; // Whether the query has finished
let failed = false; // has query failed
onMount(async () => {
    try {
        const responses = (await $cubeClient.load(query.query)).series();
        
        console.log(responses)

        const data: ChartData = { 
            labels: responses[0].series.map(entry => entry.x),      // All datasets should have the same values as x
            datasets: responses.map((s, i) => { 
                const color: string = query.colors == undefined ? randomColor() : query.colors[i] || randomColor();

                return {
                    label: s.title.split(',')[0],
                    borderColor: color, 
                    backgroundColor: color,
                    data: s.series.map(e => e.value)
                }
            })
        }
        chart = new Chart(chartElem, {
            type: 'line',
            data,
            options: { // TODO: fit content, better legend
                // responsive: true,
                // aspectRatio: 1.5
            }
        })
        
        loading = false;
    } catch {
        failed = true;
        loading = false;
    }
});
</script>

<!-- TODO: fit content in not hardcoded size -->
<div class="container relative">
    <canvas bind:this={chartElem} height="400px" width="1000px" hidden={loading||failed}></canvas>
</div>

{#if loading}
<p class='p-5'>Loading...</p>
{:else if failed}
<p class='p-5 text-red-500'>Failed</p>
{/if}