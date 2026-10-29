import re

# ============================================================
# БЕЗПЕЧНЕ ВВЕДЕННЯ
# ============================================================
def safe_int(prompt, min_val=None, max_val=None):
    while True:
        raw = input(prompt).strip()
        if not re.fullmatch(r"-?\d+", raw):
            print("  ⚠ Введіть ціле число.")
            continue
        v = int(raw)
        if min_val is not None and v < min_val:
            print(f"  ⚠ Має бути >= {min_val}.")
            continue
        if max_val is not None and v > max_val:
            print(f"  ⚠ Має бути <= {max_val}.")
            continue
        return v


def safe_int_list(prompt, elem_min, elem_max, max_len=100000):
    while True:
        raw = input(prompt).strip()
        if raw == "":
            return []
        parts = [p for p in re.split(r"[,\s]+", raw) if p]
        ok = True
        values = []
        for p in parts:
            if not re.fullmatch(r"-?\d+", p):
                print(f"  ⚠ '{p}' — не ціле число.")
                ok = False
                break
            v = int(p)
            if not (elem_min <= v <= elem_max):
                print(f"  ⚠ {v} поза діапазоном [{elem_min}, {elem_max}].")
                ok = False
                break
            values.append(v)
        if not ok:
            continue
        if len(values) > max_len:
            print(f"  ⚠ Забагато елементів (макс {max_len}).")
            continue
        return values


# ============================================================
# 1. Максимальна кількість повторень 1
# ============================================================
def find_max_consecutive_ones(nums):
    best = cur = 0
    for x in nums:
        if x == 1:
            cur += 1
            if cur > best:
                best = cur
        else:
            cur = 0
    return best


def run_task1():
    nums = safe_int_list("  nums (0/1, 1..100000 елементів): ",
                         elem_min=0, elem_max=1, max_len=100000)
    while len(nums) < 1:
        print("  ⚠ Потрібен хоча б 1 елемент.")
        nums = safe_int_list("  nums (0/1, 1..100000 елементів): ",
                             elem_min=0, elem_max=1, max_len=100000)
    print(f"  Output: {find_max_consecutive_ones(nums)}")


# ============================================================
# 2. Числа з парною кількістю цифр
# ============================================================
def find_numbers(nums):
    count = 0
    for x in nums:
        digits = len(str(abs(x)))
        if digits % 2 == 0:
            count += 1
    return count


def run_task2():
    nums = safe_int_list("  nums (1..100000, 1..500 елементів): ",
                         elem_min=1, elem_max=100000, max_len=500)
    while len(nums) < 1:
        print("  ⚠ Потрібен хоча б 1 елемент.")
        nums = safe_int_list("  nums (1..100000, 1..500 елементів): ",
                             elem_min=1, elem_max=100000, max_len=500)
    print(f"  Output: {find_numbers(nums)}")


# ============================================================
# 3. Квадрати відсортованого масиву
# ============================================================
def sorted_squares(nums):
    n = len(nums)
    result = [0] * n
    left, right = 0, n - 1
    pos = n - 1
    while left <= right:
        if abs(nums[left]) > abs(nums[right]):
            result[pos] = nums[left] * nums[left]
            left += 1
        else:
            result[pos] = nums[right] * nums[right]
            right -= 1
        pos -= 1
    return result


def run_task3():
    nums = safe_int_list("  nums (відсортований, -10000..10000, 1..10000 ел.): ",
                         elem_min=-10000, elem_max=10000, max_len=10000)
    while len(nums) < 1:
        print("  ⚠ Потрібен хоча б 1 елемент.")
        nums = safe_int_list("  nums (відсортований, -10000..10000): ",
                             elem_min=-10000, elem_max=10000, max_len=10000)
    if any(nums[i] > nums[i + 1] for i in range(len(nums) - 1)):
        print("  ⚠ Увага: масив не відсортований за неспаданням!")
    print(f"  Output: {sorted_squares(nums)}")


# ============================================================
# 4. Подвійні нулі
# ============================================================
def duplicate_zeros(arr):
    n = len(arr)
    result = []
    for x in arr:
        if x == 0:
            result.append(0)
            result.append(0)
        else:
            result.append(x)
    return result[:n]


def run_task4():
    arr = safe_int_list("  arr (0..9, 1..10000 елементів): ",
                        elem_min=0, elem_max=9, max_len=10000)
    while len(arr) < 1:
        print("  ⚠ Потрібен хоча б 1 елемент.")
        arr = safe_int_list("  arr (0..9, 1..10000 елементів): ",
                            elem_min=0, elem_max=9, max_len=10000)
    print(f"  Output: {duplicate_zeros(arr)}")


# ============================================================
# 5. Об'єднати відсортований масив
# ============================================================
def merge(nums1, m, nums2, n):
    i, j, k = m - 1, n - 1, m + n - 1
    while i >= 0 and j >= 0:
        if nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1
    while j >= 0:
        nums1[k] = nums2[j]
        j -= 1
        k -= 1
    return nums1


def run_task5():
    print("  nums1 має довжину m+n; перші m — реальні, останні n — нулі.")
    while True:
        nums1 = safe_int_list("  nums1 (-10..10, 1..200 елементів): ",
                              elem_min=-10, elem_max=10, max_len=200)
        if len(nums1) < 1:
            print("  ⚠ nums1 не може бути порожнім.")
            continue
        m = safe_int(f"  m (0..{len(nums1)}, 1 <= m+n <= 200): ",
                     min_val=0, max_val=len(nums1))
        n = len(nums1) - m
        nums2 = safe_int_list(f"  nums2 ({n} елементів, -10..10): ",
                              elem_min=-10, elem_max=10, max_len=n)
        if len(nums2) != n:
            print(f"  ⚠ nums2 має містити рівно {n} елемент(ів).")
            continue
        if m + n < 1 or m + n > 200:
            print("  ⚠ Потрібно 1 <= m+n <= 200.")
            continue
        result = merge(nums1[:], m, nums2, n)
        print(f"  Output: {result}")
        return


# ============================================================
# 6. Видалити дублікати з відсортованого масиву
# ============================================================
def remove_duplicates(nums):
    if not nums:
        return 0
    k = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[k - 1]:
            nums[k] = nums[i]
            k += 1
    return k


def run_task6():
    nums = safe_int_list("  nums (відсортований, -100..100, 1..30000 ел.): ",
                         elem_min=-100, elem_max=100, max_len=30000)
    while len(nums) < 1:
        print("  ⚠ Потрібен хоча б 1 елемент.")
        nums = safe_int_list("  nums (відсортований, -100..100): ",
                             elem_min=-100, elem_max=100, max_len=30000)
    if any(nums[i] > nums[i + 1] for i in range(len(nums) - 1)):
        print("  ⚠ Увага: масив не відсортований за неспаданням!")
    work = nums[:]
    k = remove_duplicates(work)
    print(f"  Output: k = {k}, nums = {work[:k]}")


# ============================================================
# 7. Перевірте, чи існують N і його подвійник
# ============================================================
def check_if_exist(arr):
    seen = set()
    for x in arr:
        if 2 * x in seen or (x % 2 == 0 and x // 2 in seen):
            return True
        seen.add(x)
    return False


def run_task7():
    arr = safe_int_list("  arr (-1000..1000, 2..500 елементів): ",
                        elem_min=-1000, elem_max=1000, max_len=500)
    while len(arr) < 2:
        print("  ⚠ Потрібно щонайменше 2 елементи.")
        arr = safe_int_list("  arr (-1000..1000, 2..500 елементів): ",
                            elem_min=-1000, elem_max=1000, max_len=500)
    result = check_if_exist(arr)
    print(f"  Output: {str(result).lower()}")


# ============================================================
# 8. Дійсний гірський масив
# ============================================================
def valid_mountain_array(arr):
    n = len(arr)
    if n < 3:
        return False
    i = 0
    while i + 1 < n and arr[i] < arr[i + 1]:
        i += 1
    if i == 0 or i == n - 1:
        return False
    while i + 1 < n and arr[i] > arr[i + 1]:
        i += 1
    return i == n - 1


def run_task8():
    arr = safe_int_list("  arr (0..10000, 1..10000 елементів): ",
                        elem_min=0, elem_max=10000, max_len=10000)
    while len(arr) < 1:
        print("  ⚠ Потрібен хоча б 1 елемент.")
        arr = safe_int_list("  arr (0..10000, 1..10000 елементів): ",
                            elem_min=0, elem_max=10000, max_len=10000)
    result = valid_mountain_array(arr)
    print(f"  Output: {str(result).lower()}")


# ============================================================
# 9. Замініть елементи на найбільший елемент з правого боку
# ============================================================
def replace_elements(arr):
    n = len(arr)
    result = [-1] * n
    max_right = -1
    for i in range(n - 1, -1, -1):
        result[i] = max_right
        if arr[i] > max_right:
            max_right = arr[i]
    return result


def run_task9():
    arr = safe_int_list("  arr (1..100000, 1..10000 елементів): ",
                        elem_min=1, elem_max=100000, max_len=10000)
    while len(arr) < 1:
        print("  ⚠ Потрібен хоча б 1 елемент.")
        arr = safe_int_list("  arr (1..100000, 1..10000 елементів): ",
                            elem_min=1, elem_max=100000, max_len=10000)
    print(f"  Output: {replace_elements(arr)}")


# ============================================================
# 10. Відсортувати масив за парністю
# ============================================================
def sort_array_by_parity(nums):
    return [x for x in nums if x % 2 == 0] + [x for x in nums if x % 2 != 0]


def run_task10():
    nums = safe_int_list("  nums (0..5000, 1..5000 елементів): ",
                         elem_min=0, elem_max=5000, max_len=5000)
    while len(nums) < 1:
        print("  ⚠ Потрібен хоча б 1 елемент.")
        nums = safe_int_list("  nums (0..5000, 1..5000 елементів): ",
                             elem_min=0, elem_max=5000, max_len=5000)
    print(f"  Output: {sort_array_by_parity(nums)}")


# ============================================================
# ГОЛОВНА ФУНКЦІЯ
# ============================================================
TASKS = {
    1: ("Максимальна кількість повторень 1", run_task1),
    2: ("Числа з парною кількістю цифр", run_task2),
    3: ("Квадрати відсортованого масиву", run_task3),
    4: ("Подвійні нулі", run_task4),
    5: ("Об'єднати відсортований масив", run_task5),
    6: ("Видалити дублікати з відсортованого масиву", run_task6),
    7: ("Перевірте, чи існують N і його подвійник", run_task7),
    8: ("Дійсний гірський масив", run_task8),
    9: ("Замініть елементи на найбільший елемент з правого боку", run_task9),
    10: ("Відсортувати масив за парністю", run_task10),
}


def main():
    print("=" * 55)
    print("Доступні задачі:")
    for k, (title, _) in TASKS.items():
        print(f"  {k:>2}. {title}")
    print("=" * 55)

    task_num = safe_int("Оберіть задачу (1..10): ", min_val=1, max_val=10)
    title, runner = TASKS[task_num]
    print(f"\n--- Задача {task_num}: {title} ---")
    runner()


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nПерервано.")