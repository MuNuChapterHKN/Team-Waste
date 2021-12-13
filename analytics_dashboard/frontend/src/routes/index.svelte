<script>
import BinStats from "$lib/BinStats.svelte";

</script>
<h1 class='text-2xl font-medium mt-4' >
    This is the homepage
</h1>


<div class='grid grid-cols-6 w-full items-center'>
    <div class='col-span-full text-center'>
        <BinStats />
    </div>
</div>


<style>
    .p-3 {
        background: #000;
        border-radius: 5px;
        margin: 3px;
        color:cyan;
    }
</style>