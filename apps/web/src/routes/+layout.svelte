<script lang="ts">
    import { setContext } from "svelte";
    import "../app.css";
    import { Toaster } from "svelte-sonner";
    let { data, children } = $props();
    setContext("supabase", data.supabase);
</script>

<svelte:head>
    <title>ConfirMed</title>
</svelte:head>

<Toaster />
{@render children()}
