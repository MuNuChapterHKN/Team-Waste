<script>
import { onMount } from "svelte";

import { cubeClient } from "./stores";


    let count = 0;

    onMount(async () => {
        let result = await $cubeClient.load({
            measures: ['Bin.count']
        });
        
        console.log(result.series());

        count = result.series()[0].series[0].value
})
</script>


<div class="stats shadow">
    <div class="stat">
        <div class='stat-title'>Total number of bins</div>
        <div class='stat-value'>{count}</div>
    </div>
</div>