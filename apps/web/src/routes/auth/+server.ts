import { redirect } from "@sveltejs/kit";

export const GET = async (event) => {
    const {
        url,
        locals: { supabase }
    } = event;
    const code = url.searchParams.get("code") as string;

    if (code) {
        const { error } = await supabase.auth.exchangeCodeForSession(code);
        if (!error) {
            throw redirect(303, `/home`);
        }
    }

    throw redirect(303, "/");
};
