<script lang="ts">
    import { goto } from "$app/navigation";
    import Button from "$lib/components/ui/button/button.svelte";
    import Plus from "$lib/icons/Plus.svelte";
    import type { SupabaseClient } from "@supabase/supabase-js";
    import { getContext } from "svelte";

    const supabase = getContext<SupabaseClient>("supabase");
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
                        goto("/");
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
        <section id="alerts"></section>
        <section id="patients"></section>
    </main>
</div>
