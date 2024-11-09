export const warnings = [
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

export const reports = [
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

type Alert = "None" | "Warning" | "Report";

type Patient = {
    id: number;
    name: string;
    alert: Alert;
    medications: string[];
};

export const patients: Patient[] = [
    {
        id: 1,
        name: "Sakuya Izayoi",
        alert: "None",
        medications: ["sertraline", "escitalopram"]
    },
    {
        id: 2,
        name: "Remilia Scarlet",
        alert: "None",
        medications: ["fish oil"]
    },
    {
        id: 3,
        name: "Patchouli Knowledge",
        alert: "None",
        medications: ["ciprofloxacin"]
    },
    {
        id: 4,
        name: "Alice Margatroid",
        alert: "Warning",
        medications: ["acetaminophen"]
    },
    {
        id: 5,
        name: "Flandre Scarlet",
        alert: "Warning",
        medications: ["ibuprofen"]
    },
    {
        id: 6,
        name: "Reimu Hakurei",
        alert: "Report",
        medications: ["acetaminophen"]
    },
    {
        id: 7,
        name: "Marisa Kirisame",
        alert: "Report",
        medications: ["ibuprofen"]
    },
    {
        id: 8,
        name: "Youmu Konpaku",
        alert: "None",
        medications: ["amoxicillin"]
    },
    {
        id: 9,
        name: "Yuyuko Saigyouji",
        alert: "None",
        medications: ["atorvastatin"]
    },
    {
        id: 10,
        name: "Yukari Yakumo",
        alert: "None",
        medications: ["lisinopril"]
    }
];
