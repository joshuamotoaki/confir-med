<script lang="ts">
    import Button from "$lib/components/ui/button/button.svelte";
    import Edit from "$lib/icons/Edit.svelte";
    import * as Tooltip from "$lib/components/ui/tooltip";

    let patientName = "Alice Margatroid";

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
</script>

<div>
    <div class="cont py-2">
        <div class="btw-flex">
            <h1 class="text-2xl font-semibold text-blue-800">
                Patient: {patientName}
            </h1>
            <Button>
                <Edit />
                <span> Edit Patient </span>
            </Button>
        </div>
        <main></main>
        <article id="chart">
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
        @apply size-6 rounded-sm;
    }
</style>
