<script lang="ts">
    import Button from "$lib/components/ui/button/button.svelte";
    import Edit from "$lib/icons/Edit.svelte";

    let patientName = "Alice Margatroid";
</script>

<div>
    <div class="cont py-2">
        <div class="btw-flex">
            <h1 class="text-2xl font-semibold text-blue-800">
                Patient: {patientName}
            </h1>
            <Button>
                <Edit />
                <span> Edit Patient </span>
            </Button>
        </div>
        <main></main>
        <article id="chart"></article>
    </div>
</div>
