import axios from "axios";

const api = axios.create({
    baseURL: "http://localhost:8000",
});

export async function uploadResume(file, role) {

    const formData = new FormData();

    formData.append("file", file);
    formData.append("target_role", role);

    const response = await api.post(
        "/resume-career",
        formData,
        {
            headers: {
                "Content-Type": "multipart/form-data",
            },
        }
    );

    return response.data;
}

export default api;