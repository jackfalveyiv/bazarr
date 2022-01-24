import reactRefresh from "@vitejs/plugin-react-refresh";
import path from "path";
import { defineConfig, loadEnv } from "vite";
import { findApiKey } from "./config/api-key";
import chunks from "./config/chunks";

export default defineConfig(async ({ mode, command }) => {
  const env = loadEnv(mode, process.cwd());
  const target = env.VITE_PROXY_URL;
  const allowWs = env.VITE_ALLOW_WEBSOCKET === "true";
  const secure = env.VITE_PROXY_SECURE === "true";

  if (command === "serve" && env["VITE_API_KEY"] === undefined) {
    const apiKey = await findApiKey(env);
    process.env["VITE_API_KEY"] = apiKey ?? "UNKNOWN_API_KEY";
  }

  return {
    plugins: [reactRefresh()],
    base: "./",
    resolve: {
      alias: {
        "@": path.resolve(__dirname, "./src"),
      },
    },
    build: {
      manifest: true,
      sourcemap: mode === "development",
      outDir: "./build",
      rollupOptions: {
        output: {
          manualChunks: chunks,
        },
      },
    },
    server: {
      proxy: {
        "^/(api|images|test|bazarr.log)/.*": {
          target,
          changeOrigin: true,
          secure,
          ws: allowWs,
        },
      },
    },
  };
});
