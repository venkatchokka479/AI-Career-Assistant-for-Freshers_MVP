const cards = [
  { label: 'Semantic Match Score', value: '86.4%' },
  { label: 'Skill Gap', value: '22%' },
  { label: 'Missing Skills', value: 'Kubernetes, Redis' },
  { label: 'Interview Readiness', value: 'Moderate' },
];

export default function Dashboard() {
  return (
    <main className="mx-auto min-h-screen max-w-5xl p-8">
      <h1 className="text-3xl font-semibold">AI ATS Dashboard (Freshers)</h1>
      <p className="mt-2 text-slate-300">Semantic job matching, skill gaps, and AI guidance.</p>

      <div className="mt-8 grid gap-4 md:grid-cols-2">
        {cards.map((card) => (
          <div key={card.label} className="rounded-lg border border-slate-800 bg-slate-900 p-5">
            <p className="text-sm text-slate-400">{card.label}</p>
            <p className="mt-2 text-xl font-medium">{card.value}</p>
          </div>
        ))}
      </div>
    </main>
  );
}
