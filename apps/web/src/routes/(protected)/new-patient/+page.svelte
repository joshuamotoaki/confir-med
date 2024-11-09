<script>
    import Button from "$lib/components/ui/button/button.svelte";
    import Input from "$lib/components/ui/input/input.svelte";
    import { Label } from "$lib/components/ui/label";

    let name = "";

    const handleSubmit = async () => {};
</script>

<main>
    <div class="cont py-2">
        <h2 class="text-2xl font-semibold text-blue-800">Add New Patient</h2>

        <div>
            <div class="mt-4 space-y-2">
                <div class="grid w-full max-w-sm items-center gap-1.5">
                    <Label for="name">Patient Name</Label>
                    <Input
                        bind:value={name}
                        type="text"
                        name="name"
                        placeholder="Name" />
                </div>
            </div>

            <Button onclick={handleSubmit} class="mt-4">Add Patient</Button>
        </div>
    </div>
</main>
