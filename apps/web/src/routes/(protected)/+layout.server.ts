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
                redirectTo: "http://localhost:5173/auth/"
            }
        });

        if (error) {
            console.error("error", error);
            return { status: 500, error: new Error("An error occurred") };
        }

        if (data.url) {
            redirect(303, data.url);
        }
    }
};
