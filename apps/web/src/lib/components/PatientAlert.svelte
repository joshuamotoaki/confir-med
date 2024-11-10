<script lang="ts">
    import * as Alert from "$lib/components/ui/alert/";
    import Close from "$lib/icons/Close.svelte";
    import Info from "$lib/icons/Info.svelte";
    import Warning from "$lib/icons/Warning.svelte";
    import { fade } from "svelte/transition";

    type Message = {
        id: number;
        patient: string;
        message: string;
    };

    interface Props {
        alerts: Message[];
        type: "warning" | "report";
    }

    const { alerts, type }: Props = $props();

    let visible = $state(true);
</script>

{#if visible}
    <div out:fade={{ duration: 200 }}>
        <Alert.Root variant={type === "warning" ? "destructive" : "default"}>
            <button
                class="absolute right-2 top-2"
                aria-label="Close"
                onclick={() => {
                    visible = false;
                }}>
                {#if type === "warning"}
                    <Close
                        className="size-4 text-red-500 hover:text-red-700 duration-150" />
                {:else if type === "report"}
                    <Close
                        className="size-4 text-stone-500 hover:text-stone-700 duration-150" />
                {/if}
            </button>

            <Alert.Title>
                <div class="justiyf-start flex items-center gap-1">
                    {#if type === "warning"}
                        <Warning className="size-5" />
                        <h2 class="font-semibold">Warnings</h2>
                    {:else if type === "report"}
                        <Info className="size-5" />
                        <h2 class="font-semibold">Reports</h2>
                    {/if}
                </div>
            </Alert.Title>
            <Alert.Description variant="">
                <div class="text-sm">
                    {#each alerts as alert (alert.id)}
                        <div>
                            <p>
                                {alert.patient}: {alert.message}
                            </p>
                        </div>
                    {/each}
                </div>
            </Alert.Description>
        </Alert.Root>
    </div>
{/if}
