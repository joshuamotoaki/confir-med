<script lang="ts">
    import { goto } from "$app/navigation";
    import Button from "$lib/components/ui/button/button.svelte";
    import Plus from "$lib/icons/Plus.svelte";
    import type { SupabaseClient } from "@supabase/supabase-js";
    import { getContext } from "svelte";
    import { toast } from "svelte-sonner";
    import PatientAlert from "$lib/components/PatientAlert.svelte";
    import * as Table from "$lib/components/ui/table/index.js";
    import { patients, reports, warnings } from "$lib/tmp";

    const supabase = getContext<SupabaseClient>("supabase");

    const formatMedications = (medications: string[]) => {
        return medications
            .sort()
            .map((x) => x.slice(0, 1).toUpperCase() + x.slice(1))
            .join(", ");
    };

    const formatRowColor = (alert: string) => {
        switch (alert) {
            case "Report":
                return "bg-yellow-100 hover:bg-yellow-200";
            case "Warning":
                return "bg-red-100 hover:bg-red-200";
            default:
                return "";
        }
    };

    // Sort by Id, then place warnings first, then reports
    const sortedPatients = patients.toSorted((a, b) => {
        const alertPriority = {
            Warning: 0,
            Report: 1,
            None: 2
        };
        if (alertPriority[a.alert] !== alertPriority[b.alert]) {
            return alertPriority[a.alert] - alertPriority[b.alert];
        }
        return a.id - b.id;
    });
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
        <div class="cont space-y-4 py-2">
            <section id="alerts" class="space-y-2">
                <PatientAlert alerts={warnings} type="warning" />
                <PatientAlert alerts={reports} type="report" />
            </section>
            <section id="patients">
                <Table.Root>
                    <Table.Header>
                        <Table.Row>
                            <Table.Head>Patient</Table.Head>
                            <Table.Head>Alert</Table.Head>
                            <Table.Head>Medications</Table.Head>
                        </Table.Row>
                    </Table.Header>
                    <Table.Body>
                        {#each sortedPatients as patient (patient.id)}
                            <Table.Row class={formatRowColor(patient.alert)}>
                                <Table.Cell class="font-medium"
                                    >{patient.name}</Table.Cell>
                                <Table.Cell>{patient.alert}</Table.Cell>
                                <Table.Cell
                                    >{formatMedications(
                                        patient.medications
                                    )}</Table.Cell>
                                <Table.Cell class="text-right">
                                    <Button
                                        size="sm"
                                        variant="secondary"
                                        href={`/patients/${patient.id}`}
                                        aria-label={`View ${patient.name}'s profile`}
                                        >View</Button>
                                </Table.Cell>
                            </Table.Row>
                        {/each}
                    </Table.Body>
                </Table.Root>
            </section>
        </div>
    </main>
</div>
