<script lang="ts">
    import { setContext } from "svelte";
    import "../app.css";
    let { data, children } = $props();
    setContext("supabase", data.supabase);
</script>

{@render children()}
