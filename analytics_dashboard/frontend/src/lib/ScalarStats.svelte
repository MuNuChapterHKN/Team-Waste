<script lang='typescript'>
    import type { ScalarQuery } from '../types/scalar_query.type'
    import { cubeClient } from './stores';
    
    export let queries: Array<ScalarQuery>;

    let getResults = async () => Promise.all(queries
            .map(async (q) => {
                return {
                    title: q.title,
                    value: (await $cubeClient.load(q.query)).series()[0].series[0].value // The series contains just one value
                }
            }))
</script>

{#await getResults()}

<div class="btn loading">Loading</div>

{:then list} 

<div class="stats shadow">
    {#each list as single}
    <div class='stat'>
        <div class='stat-title'>{single.title}</div>
        <div class='stat-value'>{single.value}</div>
    </div>
    {/each}

</div>

{/await}