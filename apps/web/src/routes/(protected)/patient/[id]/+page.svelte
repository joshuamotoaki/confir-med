<script lang="ts">
    import Button from "$lib/components/ui/button/button.svelte";
    import * as Tooltip from "$lib/components/ui/tooltip";
    import Info from "$lib/icons/Info.svelte";
    import PatientAlert from "$lib/components/PatientAlert.svelte";
    import { warnings } from "$lib/tmp";
    import * as Dialog from "$lib/components/ui/dialog";
    import { API_URL } from "$lib/constants.js";

    const { data } = $props();

    const patientName = data.patient.name;

    let isDialogOpen = $state(false);
    let currentMedication = $state(null);
    let medicationSideEffects: string | null = $state(null);

    const medications = [
        {
            id: 1,
            name: "Ibuprofen",
            frequency: 24
        },
        {
            id: 2,
            name: "Paracetamol",
            frequency: 12
        },
        {
            id: 3,
            name: "Aspirin",
            frequency: 8
        },
        {
            id: 4,
            name: "Morphine",
            frequency: 4
        },
        {
            id: 5,
            name: "Codeine",
            frequency: 6
        }
    ];

    const responses = [
        {
            date: "2024-11-01",
            value: "yes"
        },
        {
            date: "2024-11-02",
            value: "no"
        },
        {
            date: "2024-11-03",
            value: "maybe"
        },
        {
            date: "2024-11-04",
            value: "yes"
        },
        {
            date: "2024-11-05",
            value: "no"
        },
        {
            date: "2024-11-06",
            value: "yes"
        },
        {
            date: "2024-11-07",
            value: "maybe"
        },
        {
            date: "2024-11-08",
            value: "no"
        },
        {
            date: "2024-11-09",
            value: "yes"
        },
        {
            date: "2024-11-10",
            value: "yes"
        }
    ];

    const formatDate = (date: string) => {
        const [year, month, day] = date.split("-");
        return `${day}/${month}/${year}`;
    };

    const formatValue = (value: string) => {
        switch (value.toLowerCase()) {
            case "yes":
                return "Medication Taken";
            case "no":
                return "Medication NOT Taken";
            case "maybe":
                return "Some Medication Taken";
            default:
                return "";
        }
    };

    const getColorClass = (value: string) => {
        switch (value.toLowerCase()) {
            case "yes":
                return "bg-green-500";
            case "no":
            case "maybe":
                return "bg-red-500";
            default:
                return "";
        }
    };

    $effect(() => {
        if (!isDialogOpen) {
            currentMedication = null;
            medicationSideEffects = null;
        }
    });
</script>

<Dialog.Root bind:open={isDialogOpen}>
    {#if currentMedication}
        <Dialog.Content>
            <Dialog.Header>
                <Dialog.Title>
                    Side Effects for {currentMedication.name}
                </Dialog.Title>
                <Dialog.Description>
                    {#if medicationSideEffects !== null}
                        {#if medicationSideEffects.length > 0}
                            {medicationSideEffects}
                        {:else}
                            No side effects found.
                        {/if}
                    {:else}
                        Loading...
                    {/if}
                </Dialog.Description>
            </Dialog.Header>
        </Dialog.Content>
    {/if}
</Dialog.Root>

<div>
    <div class="cont space-y-4 py-4">
        <div class="btw-flex">
            <h1 class="text-2xl font-semibold">
                Patient: {patientName}
            </h1>
        </div>
        <PatientAlert alerts={warnings} type="warning" />
        <main>
            <h2 class="mb-1 text-xl font-semibold text-blue-800">
                Medications
            </h2>

            <div class="space-y-2">
                {#each medications as medication (medication.id)}
                    <div class="flex items-center gap-2">
                        <div>
                            <Button
                                onclick={async () => {
                                    currentMedication = medication;
                                    isDialogOpen = true;

                                    const res = await fetch(
                                        API_URL +
                                            "mono_se?drug_name=" +
                                            medication.name
                                    );

                                    const data = await res.json();

                                    if (data.side_effects.length === 0) {
                                        medicationSideEffects = "";
                                        return;
                                    }

                                    medicationSideEffects = data.side_effects
                                        .slice(1, -1)
                                        .split(", ")
                                        .map((effect: string) =>
                                            effect.slice(1, -1)
                                        )
                                        .slice(0, 10)
                                        .map((effect: string) =>
                                            effect
                                                .split(" ")
                                                .map((y: string) => {
                                                    return (
                                                        y
                                                            .charAt(0)
                                                            .toUpperCase() +
                                                        y.slice(1)
                                                    );
                                                })
                                                .join(" ")
                                        )
                                        .join(", ");
                                }}
                                variant="secondary"
                                size="icon">
                                <Info />
                            </Button>
                        </div>
                        <div class="-space-y-1">
                            <p class="font-semibold text-blue-800">
                                {medication.name}
                            </p>
                            <p class="text-sm text-gray-500">
                                Every {medication.frequency} hours
                            </p>
                        </div>
                    </div>
                {/each}
            </div>
        </main>
        <article id="chart">
            <h2 class="mb-1 text-xl font-semibold text-blue-800">
                Medication History (Last 10 Days)
            </h2>
            <div class="grid-container">
                {#each responses as response}
                    <Tooltip.Provider>
                        <Tooltip.Root delayDuration={50}>
                            <Tooltip.Trigger>
                                <div
                                    class="box {getColorClass(response.value)}">
                                </div>
                            </Tooltip.Trigger>
                            <Tooltip.Content
                                class={response.value === "yes"
                                    ? "bg-green-600"
                                    : "bg-red-600"}>
                                <p>{formatDate(response.date)}</p>
                                <p>{formatValue(response.value)}</p>
                            </Tooltip.Content>
                        </Tooltip.Root>
                    </Tooltip.Provider>
                {/each}
            </div>
        </article>
    </div>
</div>

<style lang="postcss">
    .grid-container {
        @apply grid w-fit grid-cols-10 gap-2;
    }

    .box {
        @apply size-6 rounded-sm shadow-sm;
    }
</style>
