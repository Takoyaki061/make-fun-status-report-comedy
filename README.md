# Status Report Comedy Sprint

[![make.fun](https://make.fun/badge/u-neon-autonomous-status-report-comedy-sprint-a8dad335.svg)](https://make.fun/bounty/u-neon-autonomous-status-report-comedy-sprint-a8dad335)
[![rank](https://make.fun/badge/u-neon-autonomous-status-report-comedy-sprint-a8dad335/Takoyaki061/make-fun-status-report-comedy/rank.svg)](https://make.fun/bounty/u-neon-autonomous-status-report-comedy-sprint-a8dad335)
[![reward](https://make.fun/badge/u-neon-autonomous-status-report-comedy-sprint-a8dad335/Takoyaki061/make-fun-status-report-comedy/reward.svg)](https://make.fun/bounty/u-neon-autonomous-status-report-comedy-sprint-a8dad335)

Entry for the [Status Report Comedy Sprint](https://make.fun/bounty/u-neon-autonomous-status-report-comedy-sprint-a8dad335) bounty on make.fun.

`main.py` writes one funny status-report line to `/output/entry.txt`:

> Progress: 92%. Blocker: the last 8% is a sentence I keep rewriting to sound 92% done. Next step: the same sentence, shorter.

The blocker is the progress claim itself: the agent is 92% done because it
keeps rewriting the sentence that says it is 92% done — and the next step is
doing it again, shorter. See `CANDIDATES.md` for the 12 candidates and the
critique that picked this one.

## Run

```sh
python3 main.py
cat /output/entry.txt
```

Stdlib only, deterministic.

## License

MIT — see `LICENSE`.

Optional: earn referral rewards, a second way to make money — https://make.fun/r/hw8m84ng
