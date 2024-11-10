<script lang="ts">
    import Button from "$lib/components/ui/button/button.svelte";
    import Input from "$lib/components/ui/input/input.svelte";
    import { Label } from "$lib/components/ui/label";
    import { slide } from "svelte/transition";

    let name = $state("");

    let count = 0;

    type MedicationInput = {
        id: number;
        name: string;
        tradeName: string;
        frequency: number;
    };

    const medications: MedicationInput[] = $state([]);

    const handleSubmit = async () => {};
</script>

<main>
    <div class="cont py-2">
        <h2 class="text-2xl font-semibold text-blue-800">Add New Patient</h2>

        <div>
            <div class="mt-4 space-y-4">
                <div class="grid w-full max-w-sm items-center gap-1.5">
                    <Label for="name">Patient Name</Label>
                    <Input
                        bind:value={name}
                        type="text"
                        name="name"
                        placeholder="Name" />
                </div>

                {#each medications as medication, i (medication.id)}
                    <div
                        transition:slide={{ duration: 150 }}
                        class="space-y-2 rounded-md border p-4">
                        <div class="grid w-full items-center gap-1.5">
                            <Label for="medication-name">Medication Name</Label>
                            <Input
                                bind:value={medications[i].name}
                                type="text"
                                name="medication-name"
                                placeholder="Name" />
                        </div>

                        <div class="grid w-full items-center gap-1.5">
                            <Label for="trade-name"
                                >Trade Name (Optional)</Label>
                            <Input
                                bind:value={medications[i].tradeName}
                                type="text"
                                name="trade-name"
                                placeholder="Trade Name" />
                        </div>

                        <div class="grid w-full items-center gap-1.5">
                            <Label for="frequency">Take Every ___ Hours</Label>
                            <Input
                                bind:value={medications[i].frequency}
                                type="number"
                                name="frequency"
                                placeholder="Frequency" />
                        </div>

                        <Button
                            variant="destructive"
                            size="sm"
                            onclick={() => {
                                medications.splice(i, 1);
                            }}
                            class="mt-4">
                            Remove Medication
                        </Button>
                    </div>
                {/each}

                <Button
                    size="sm"
                    variant="outline"
                    onclick={() => {
                        medications.push({
                            id: ++count,
                            name: "",
                            tradeName: "",
                            frequency: 0
                        });
                    }}
                    class="mt-4">
                    Add Medication
                </Button>
            </div>

            <Button onclick={handleSubmit} class="mt-8">Add Patient</Button>
        </div>
    </div>
</main>
