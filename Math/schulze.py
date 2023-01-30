"""
Ranks candidates by the Schulze method.
For more information read http://en.wikipedia.org/wiki/Schulze_method.
"""

__author__ = "Bulat I. Nasyrov"
__contact__ = "bulatnasirov2003@gmail.com"

from collections import defaultdict


def _add_remaining_ranks(d, name, remaining_ranks, weight):
	for remaining_rank in remaining_ranks:
		for other_name in remaining_rank:
			d[name, other_name] += weight


def _add_ranks_to_d(d, ranks, weight):
	for i, rank in enumerate(ranks):
		remaining_ranks = ranks[i+1:]
		for name in rank:
			_add_remaining_ranks(d, name, remaining_ranks, weight)


# Вычисляет массив d в методе Шульце.
# d[V, M] - сила самого сильного пути от кандидата V к W.
def _compute_d(weight_ranks):
	d = defaultdict(int)
	for ranks, weight in weight_ranks:
		_add_ranks_to_d(d, ranks, weight)
	return d


# Вычисляет массив p в методе Шульце.
# p[V, M] - сила самого сильного пути от кандидата V к W.
def _compute_p(d, candidate_names):
	p = {}
	for candidate_name1 in candidate_names:
		for candidate_name2 in candidate_names:
			if candidate_name1 != candidate_name2:
				strength = d.get((candidate_name1, candidate_name2), 0)
				if strength > d.get((candidate_name2, candidate_name1), 0):
					p[candidate_name1, candidate_name2] = strength

	for candidate_name1 in candidate_names:
		for candidate_name2 in candidate_names:
			if candidate_name1 != candidate_name2:
				for candidate_name3 in candidate_names:
					if (candidate_name1 != candidate_name3) and (candidate_name2 != candidate_name3):
						curr_value = p.get((candidate_name2, candidate_name3), 0)
						new_value = min(
							p.get((candidate_name2, candidate_name1), 0),
							p.get((candidate_name1, candidate_name3), 0))
						if new_value > curr_value:
							p[candidate_name2, candidate_name3] = new_value
	return p


# Ранжирует кандидатов по p
def _rank_p(candidate_names, p):
	candidate_wins = defaultdict(list)

	for candidate_name1 in candidate_names:
		num_wins = 0

		# Вычислите количество побед этого кандидата над всеми другими кандидатами.
		for candidate_name2 in candidate_names:
			if candidate_name1 == candidate_name2:
				continue
			candidate1_score = p.get((candidate_name1, candidate_name2), 0)
			candidate2_score = p.get((candidate_name2, candidate_name1), 0)
			if candidate1_score > candidate2_score:
				num_wins += 1

		candidate_wins[num_wins].append(candidate_name1)
	sorted_wins = sorted(candidate_wins.iterkeys(), reverse=True)
	return [candidate_wins[num_wins] for num_wins in sorted_wins]


def compute_ranks(candidate_names, weighted_ranks):
	"""
	Параметр candidate_names - это последовательность, содержащая все имена кандидатов.
	Параметр weighted_ranks - это последовательность пар (ранги, вес).
	Первый элемент, ранги, представляет собой ранжирование кандидатов.
	Это массив массивов, так что мы можем выражать связи.

	Например, [[a, b], [c], [d, e]] представляет a = b > c > d = e.
	Второй элемент, вес, обычно представляет собой количество избирателей, выбравших этот рейтинг.
	"""
	d = _compute_d(weight_ranks)
	p = _compute_p(d, candidate_names)
	return _rank_p(candidate_names, p)
