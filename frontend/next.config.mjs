/** @type {import('next').NextConfig} */
const nextConfig = {
  output: 'export',
  // disable image optimization since we are using static export
  images: {
    unoptimized: true,
  },
};

export default nextConfig;
