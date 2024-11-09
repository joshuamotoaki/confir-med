<!-- 
    @component +error.svelte 

    View that renders when an error occurs.
    Based on the TigerJunction error page.
    - Author: Joshua Lau '26
-->

<script lang="ts">
    import { page } from "$app/stores";
    import Button from "$lib/components/ui/button/button.svelte";
    import Home from "$lib/icons/Home.svelte";
</script>

<svelte:head>
    <title>ConfirMed | Oh Noes!</title>
    <meta property="og:title" content="ConfirMed | Oh Noes!" />
</svelte:head>

<div id="page" class="h-screen">
    <div id="overlay" class="std-flex h-full">
        <div class="std-flex">
            <div class="text-center">
                <h1 class="text-8xl font-semibold text-primary">Oh noes!</h1>
                <h2 class="mb-8 text-4xl font-light text-slate-700">
                    {$page.status}
                    {$page.error?.message}
                </h2>
                <Button href="/" size="lg">
                    <Home />
                    <span> Go to Homepage </span>
                </Button>
            </div>
        </div>
    </div>
</div>

<style lang="postcss">
    #overlay {
        @apply bg-blue-100/40;
    }

    #page {
        background-image: url("/bg.svg");
        background-size: cover;
        background-position: center;
    }
</style>
