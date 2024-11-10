export const load = async ({ locals, params }) => {
    const id = params.id;
    const user = await locals.supabase.auth.getUser();

    const { data, error } = await locals.supabase
        .from("profiles")
        .select("*")
        .eq("id", id)
        .eq("doctor_id", user?.data?.user?.id);

    if (error) {
        console.error("error", error);
        throw new Error("An error occurred");
    }

    if (data.length === 0) {
        return { status: 404, error: new Error("Not found") };
    }

    console.log(data[0]);
    return {
        patient: data[0]
    };
};
