<script>
    import { Button } from "$lib/components/ui/button";
</script>

<div id="page" class="flex min-h-screen">
    <div id="overlay" class="flex flex-1 flex-col pb-4">
        <header class="flex h-16 border-b shadow-sm">
            <div class="cont btw-flex">
                <button
                    onclick={() => {
                        // Scroll to top
                        window.scrollTo({ top: 0, behavior: "smooth" });
                    }}>
                    <div class="flex items-end gap-1 font-semibold">
                        <h2 class="text-xl">ConfirMed</h2>
                    </div>
                </button>
                <nav>
                    <Button size="sm" href="/home">
                        <span> Get Started </span>
                    </Button>
                </nav>
            </div>
        </header>
        <main class="std-flex flex-1">
            <div class="cont std-flex flex-col space-y-16 py-12">
                <div class="space-y-4 text-center">
                    <h1
                        class="text-6xl font-semibold leading-tight text-slate-900">
                        IDENTIFYING DRUGS TO HELP WITH GERIATRIC CARE!
                    </h1>
                    <p
                        class="mx-auto max-w-lg text-xl leading-relaxed text-slate-500">
                        Caption goes here and there.
                    </p>

                    <Button size="lg" href="/home">
                        <span> Get Started </span>
                    </Button>
                </div>
                <section class="grid gap-4 sm:grid-cols-3">
                    <div class="card">
                        <div class="icon">i</div>
                        <h4 class="card-title">Info 1</h4>
                        <p class="card-body">Do something here.</p>
                    </div>
                    <div class="card">
                        <div class="icon">i</div>
                        <h4 class="card-title">Info 2</h4>
                        <p class="card-body">Do something here.</p>
                    </div>
                    <div class="card">
                        <div class="icon">i</div>
                        <h4 class="card-title">Info 3</h4>
                        <p class="card-body">Do something here.</p>
                    </div>
                </section>
            </div>
        </main>
        <footer>
            <div class="cont">
                <p class="mt-4 text-center text-sm text-slate-500">
                    There is some info that goes here. <a href="/" class="link">
                        Wow look there's a link!
                    </a>
                </p>
            </div>
        </footer>
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

    .card {
        @apply space-y-1 rounded-lg border bg-gradient-to-br from-white to-slate-100 p-4 shadow-sm;
    }

    .icon {
        @apply mb-2 text-4xl text-primary;
    }

    .card-title {
        @apply text-xl font-semibold;
    }
</style>
