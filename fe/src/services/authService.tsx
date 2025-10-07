import axios from "axios";

export async function loginUser(username: string, password: string) {
  try {
    const response = await axios.post("/auth/login", { username, password });
    const { access_token, role } = response.data;

    // Store token securely
    localStorage.setItem("token", access_token);

    return { success: true, role };
  } catch (error) {
    console.error("Login failed:", error);
    return { success: false, message: "Invalid credentials" };
  }
}

interface RegisterPayload {
  username: string;
  password: string;
  role: string;
  schoolId?: string;
  curriculumTag?: string;
}

export async function registerUser(payload: RegisterPayload): Promise<{ success: boolean; message?: string }> {
  try {
    await axios.post("/auth/register", payload);
    return { success: true };
  } catch (error) {
    console.error("Registration failed:", error);
    return { success: false, message: "Could not register user" };
  }
}