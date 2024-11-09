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
        <a href="/home" class="flex items-center gap-2">
            <img src="/logo.png" class="size-9" alt="Logo" />
            <div class="-space-y-2">
                <h1 class="text-2xl font-bold text-blue-800">ConfirMed</h1>
                <h2 class="text-sm text-stone-700">Doctor Portal</h2>
            </div>
        </a>
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
            <Button variant="outline" href="/new-patient">
                <Plus />
                <span> New Patient </span>
            </Button>
        </nav>
    </div>
</header>
