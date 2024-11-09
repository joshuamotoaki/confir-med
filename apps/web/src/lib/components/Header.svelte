<script>
    import { getContext } from "svelte";
    import Button from "./ui/button/button.svelte";
    import { toast } from "svelte-sonner";
    import { goto } from "$app/navigation";
    import Plus from "$lib/icons/Plus.svelte";

    const supabase = getContext("supabase");
</script>

<header class="std-flex h-16 bg-stone-100">
    <div class="cont btw-flex">
        <div class="-space-y-2">
            <h1 class="text-2xl font-bold text-blue-800">ConfirMed</h1>
            <h2 class="text-sm text-stone-700">Doctor Portal</h2>
        </div>
        <nav class="std-flex gap-2">
            <Button variant="ghost" href="/home">
                <span> Home </span>
            </Button>
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
