<script>
    import Footer from "$lib/components/Footer.svelte";
    import Header from "$lib/components/Header.svelte";

    let { children } = $props();
</script>

<div class="flex min-h-screen flex-col">
    <Header />
    {@render children()}
    <div class="flex-1"></div>
    <Footer />
</div>
