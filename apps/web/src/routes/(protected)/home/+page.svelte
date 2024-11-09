<script lang="ts">
    import { goto } from "$app/navigation";
    import Button from "$lib/components/ui/button/button.svelte";
    import Plus from "$lib/icons/Plus.svelte";
    import type { SupabaseClient } from "@supabase/supabase-js";
    import { getContext } from "svelte";
    import { toast } from "svelte-sonner";
    import * as Alert from "$lib/components/ui/alert/";
    import Warning from "$lib/icons/Warning.svelte";
    import Info from "$lib/icons/Info.svelte";
    import Close from "$lib/icons/Close.svelte";
    import { fade } from "svelte/transition";

    const supabase = getContext<SupabaseClient>("supabase");

    let warningsVisible = true;
    let reportsVisible = true;

    const warnings = [
        {
            id: 1,
            patient: "Alice Margatroid",
            message: "Forgot to take medication (acetaminophen) on 11/9."
        },
        {
            id: 2,
            patient: "Flandre Scarlet",
            message: "Forgot to take medication (ibuprofen) on 11/9."
        }
    ];

    const reports = [
        {
            id: 1,
            patient: "Reimu Hakurei",
            message: "Side effects of medication (acetaminophen) reported."
        },
        {
            id: 2,
            patient: "Marisa Kirisame",
            message: "Side effects of medication (ibuprofen) reported."
        }
    ];
</script>

<div>
    <header class="std-flex h-16 bg-stone-100">
        <div class="cont btw-flex">
            <div class="-space-y-2">
                <h1 class="text-2xl font-bold text-blue-800">ConfirMed</h1>
                <h2 class="text-sm text-stone-700">Doctor Portal</h2>
            </div>
            <nav class="std-flex gap-2">
                <Button
                    variant="ghost"
                    onclick={async () => {
                        const { error } = await supabase.auth.signOut();
                        if (error) {
                            toast.error(
                                "There was a problem logging out. Please try again."
                            );
                        } else {
                            goto("/");
                        }
                    }}>
                    <span> Logout </span>
                </Button>
                <Button variant="outline">
                    <Plus />
                    <span> Add Patient </span>
                </Button>
            </nav>
        </div>
    </header>
    <main>
        <div class="cont py-2">
            <section id="alerts" class="space-y-2">
                {#if warningsVisible}
                    <div out:fade={{ duration: 300 }}>
                        <Alert.Root variant="destructive">
                            <button
                                class="absolute right-2 top-2"
                                aria-label="Close"
                                onclick={() => {
                                    warningsVisible = false;
                                }}>
                                <Close className="size-4 text-red-500" />
                            </button>
                            <Alert.Title>
                                <div
                                    class="justiyf-start flex items-center gap-1">
                                    <Warning className="size-5" />
                                    <h2 class=" font-semibold">Warnings</h2>
                                </div>
                            </Alert.Title>
                            <Alert.Description>
                                <div class="text-sm">
                                    {#each warnings as warning}
                                        <div>
                                            <p>
                                                {warning.patient}: {warning.message}
                                            </p>
                                        </div>
                                    {/each}
                                </div>
                            </Alert.Description>
                        </Alert.Root>
                    </div>
                {/if}

                {#if reportsVisible}
                    <div out:fade={{ duration: 300 }}>
                        <Alert.Root>
                            <button
                                class="absolute right-2 top-2"
                                aria-label="Close"
                                onclick={() => {
                                    reportsVisible = false;
                                }}>
                                <Close className="size-4 text-stone-500" />
                            </button>

                            <Alert.Title>
                                <div
                                    class="justiyf-start flex items-center gap-1">
                                    <Info className="size-5" />
                                    <h2 class="font-semibold">Reports</h2>
                                </div>
                            </Alert.Title>
                            <Alert.Description variant="">
                                <div class="text-sm">
                                    {#each reports as report}
                                        <div>
                                            <p>
                                                {report.patient}: {report.message}
                                            </p>
                                        </div>
                                    {/each}
                                </div>
                            </Alert.Description>
                        </Alert.Root>
                    </div>
                {/if}
            </section>
            <section id="patients"></section>
        </div>
    </main>
</div>

<style lang="postcss">
    article {
        @apply rounded-md p-4 shadow-md;
    }
</style>
