import { redirect } from "@sveltejs/kit";
import type { LayoutServerLoad } from "../$types";

export const load: LayoutServerLoad = async ({ locals }) => {
    const supAuth = locals.supabase.auth;
    const {
        data: { user }
    } = await supAuth.getUser();
    if (!user) {
        const { data, error } = await supAuth.signInWithOAuth({
            provider: "google",
            options: {
                redirectTo: "/auth/"
            }
        });

        if (error) {
            console.error("error", error);
            return { status: 500, error: new Error("An error occurred") };
        }

        if (data.url) {
            redirect(303, data.url);
        }
    } else {
        const { data, error } = await locals.supabase
            .from("profiles")
            .select("*")
            .eq("id", user.id);
        if (error) {
            console.error("error", error);
            throw new Error("An error occurred");
        }

        if (data.length === 0) {
            const { error } = await locals.supabase
                .from("profiles")
                .insert([{ id: user.id, name: user.user_metadata.full_name }]);
            if (error) {
                console.error("error", error);
                throw new Error("An error occurred");
            }
        }

        const patients = await locals.supabase
            .from("profiles")
            .select("id, name, alert, medications")
            .eq("doctor_id", user.id);

        return {
            profile: {
                id: user.id,
                name: user.user_metadata.full_name,
                code:
                    user.user_metadata.full_name
                        .split(" ")
                        .map((n: string) => n[0])
                        .join("") +
                    "-" +
                    user.id.slice(0, 4).toUpperCase()
            },
            patients: patients.data
        };
    }
};
