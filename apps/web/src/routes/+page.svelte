<script>
    import { Button } from "$lib/components/ui/button";
    import Info from "$lib/icons/Info.svelte";
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
                    <a href="/home" class="flex items-center gap-2">
                        <img src="/logo.png" class="size-8" alt="Logo" />
                        <div class="-space-y-2">
                            <h1 class="text-2xl font-bold text-blue-800">
                                ConfirMed
                            </h1>
                        </div>
                    </a>
                </button>
                <nav>
                    <Button href="/home">
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
                        Smarter and safer self-administration
                    </h1>
                    <p
                        class="mx-auto max-w-lg text-xl leading-relaxed text-slate-600">
                        Welcome to ConfirMed!
                    </p>

                    <Button size="lg" href="/home">
                        <span> Get Started </span>
                    </Button>
                </div>
                <section class="grid gap-4 sm:grid-cols-3">
                    <div class="card">
                        <div class="icon">
                            <Info />
                        </div>
                        <h4 class="card-title">The Issue</h4>
                        <p class="card-body">
                            In 2018, a study found that most elderly people take
                            five or more medications a day and are treated by
                            several physicians at once. When the number of
                            prescriptions rises, it is more common to confuse
                            the medications.
                            <img
                                src="/elderly_struggle_meds2.png"
                                alt="Elderly person organizing daily medication" />
                        </p>
                    </div>
                    <div class="card">
                        <div class="icon">
                            <Info />
                        </div>
                        <h4 class="card-title">
                            Further Implications of Danger
                        </h4>
                        <p class="card-body">
                            A study in 2018 found that when patients were asked
                            what they knew about the treatment they were taking,
                            the rate of correct response was about 52%
                            considering all of the medications prescribed. They
                            were most knowledgeable about which medicines they
                            were taking (75.8% of patients responded correctly
                            to this item), what the medicines were for, and how
                            to take them (67.8%). Patients were least
                            knowledgeable about the precautions they should take
                            when using their medications (with only a 3.9% rate
                            of correct responses).
                        </p>
                    </div>
                    <div class="card">
                        <div class="icon">
                            <Info />
                        </div>
                        <h4 class="card-title">Our Purpose</h4>
                        <p class="card-body">
                            ConfirMed's goal is to ensure patient safety by
                            helping individuals accurately manage medication
                            intake, and help physicians track medication intake
                            nd intervene in patienter mishaps to allow
                            self-administration be smarter and safer.
                        </p>
                    </div>
                </section>
            </div>
        </main>
        <footer>
            <div class="cont">
                <p class="mt-4 text-center text-sm text-slate-500">
                    There is some info that goes here. <a href="/" class="link">
                        Wow, look there's a link!
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
        @apply text-primary mb-2 text-4xl;
    }

    .card-title {
        @apply text-xl font-semibold;
    }
</style>
