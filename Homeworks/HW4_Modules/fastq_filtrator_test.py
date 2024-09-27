import pytest 
from <ваш скрипт> import filter_fastq
from example_data import EXAMPLE_FASTQ


def select_reads(ids):
    return {id_: EXAMPLE_FASTQ[id_] for id_ in ids}


def test_default_filter_fastq():
    assert filter_fastq(EXAMPLE_FASTQ) == EXAMPLE_FASTQ


def test_sctict_filter_fastq():
    assert filter_fastq(EXAMPLE_FASTQ, length_bounds=1) == dict()
    assert filter_fastq(EXAMPLE_FASTQ, gc_bounds=1) == dict()
    assert filter_fastq(EXAMPLE_FASTQ, quality_threshold=101) == dict()


@pytest.mark.parametrize(
    "params, expected_ids",
    [
        ({"length_bounds": (50, 75)}, ["@SRX079811", "@SRX079812"]),
        ({"gc_bounds": (55, 90)}, ["@SRX079810"]),
        ({"gc_bounds": (50, 60), "quality_threshold": 33}, ["@SRX079804", "@SRX079810"]),
    ]
)
def test_filter_fastq(params, expected_ids):
    expected = select_reads(expected_ids)
    assert filter_fastq(EXAMPLE_FASTQ, **params) == expected