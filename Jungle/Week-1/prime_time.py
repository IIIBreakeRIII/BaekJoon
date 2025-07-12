# test_sieve.py
from time_memory_complexity import measure_time, measure_memory, plot_results
from prime import find_n_primes

if __name__ == "__main__":
    print("start")
    # 측정할 n 값 리스트 (튜플 리스트 형태)
    inputs = [(5_000,), (10_000,), (20_000,), (30_000,), (40_000,)]
    print(inputs)

    # 시간 및 메모리 측정
    time_data = measure_time(find_n_primes, inputs, repeat=5, number=1)
    mem_data  = measure_memory(find_n_primes, inputs)

    # 콘솔에 결과 출력
    print("시간 측정 결과 (n, sec):")
    for args, t in time_data:
        print(f"  n={args[0]:>6} → {t:.6f} sec")

    print("\n메모리 측정 결과 (n, KB):")
    for args, m in mem_data:
        print(f"  n={args[0]:>6} → {m:.1f} KB")

    # 성장 추이를 한눈에 보기 위해 그래프로
    plot_results(
        time_data,
        mem_data,
        xlabel="n (max 값)",
        time_label="실행 시간 (초)",
        memory_label="피크 메모리 사용량 (KB)",
        title_prefix="Sieve of Eratosthenes 복잡도"
    )

