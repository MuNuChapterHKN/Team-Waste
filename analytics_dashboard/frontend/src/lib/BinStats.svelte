<script>
import { onMount } from "svelte";

import { cubeClient } from "./stores";


    let binCount = 0;
    let islandCount = 0;


    onMount(async () => {
        $cubeClient.load({
            measures: ['Bin.count']
        }).then(r => {
            binCount = r.series()[0].series[0].value
        })
        

        $cubeClient.load({
            measures: ['Island.count']
        }).then(r => {
            islandCount = r.series()[0].series[0].value
        })
    })
</script>


<div class="stats shadow ">
    <div class="stat">
        <div class='stat-title'>Number of bins</div>
        <div class='stat-value'>{binCount}</div>
    </div>
    <div class="stat">
        <div class="stat-title">Number of islands</div>
        <div class="stat-value">{islandCount}</div>
    </div>
</div>