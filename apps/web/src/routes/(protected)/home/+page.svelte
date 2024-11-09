<script lang="ts">
    import { goto } from "$app/navigation";
    import Button from "$lib/components/ui/button/button.svelte";
    import Plus from "$lib/icons/Plus.svelte";
    import type { SupabaseClient } from "@supabase/supabase-js";
    import { getContext } from "svelte";
    import { toast } from "svelte-sonner";
    import PatientAlert from "$lib/components/PatientAlert.svelte";

    const supabase = getContext<SupabaseClient>("supabase");

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
                <PatientAlert alerts={warnings} type="warning" />
                <PatientAlert alerts={reports} type="report" />
            </section>
            <section id="patients"></section>
        </div>
    </main>
</div>
