export default function CTASection({ loading }: { loading: boolean }) {
  return (
    <div className="mt-4">
      <button
        type="submit"
        className="w-full py-2 bg-blue-600 text-white rounded"
        disabled={loading}
      >
        {loading ? 'Signing in…' : 'Login'}
      </button>
    </div>
  );
}