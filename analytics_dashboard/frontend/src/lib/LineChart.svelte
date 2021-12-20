<script lang='ts'>
import { cubeClient } from '$lib/stores';

    import Chart, { ChartData, Title } from 'chart.js/auto';
    import type { TimeQuery } from 'src/types/time_query.type';
    import { onMount } from 'svelte';

    export let query: TimeQuery;
    
    
    // TODO: Get evenly spaced colors
    function randomColor() {
        return '#'+(Math.random()*0xFFFFFF<<0).toString(16);
    }

    let chartElem;
    let chart: Chart;

    onMount(async () => {
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
    });
</script>

<!--TODO: fit content in not hardcoded size -->
<canvas bind:this={chartElem} height="400px" width="1000px"></canvas>