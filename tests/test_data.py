TEST_DATA = {
    "Equal": {
        "test_true": [
            ("TestTrue", "TestTrue"),
            ("TestFalse", "TestFalse"),
        ],
        "test_false": [
            ("TestFalse", "TestTrue"),
            ("TestTrue", "TestFalse")
        ],
        "test_exception": [
            ("TestException", 100)
        ],
    },

    "NotEqual": {
        "test_true": [
            ("TestTrue", "TestFalse")
        ],
        "test_false": [
            ("TestFalse", "TestFalse")
        ],
        "test_exception": [
            ("TestException", 100)
        ],
    },

    "In": {
        "test_true": [
            (100, [100, 200]),
            ("TestTrue", ("TestTrue", "TestFalse")),
            ("TestFalse", ("TestTrue", "TestFalse")),
            ("TestTrue", ["TestTrue", "TestTrue"]),
            ("TestTrue", "TestTrue TestFalse"),
            ("TestTrue", "TestTrue,TestFalse"),
            ("TestTrue", "TestTrue, TestFalse"),
            ("TestTrue", "TestTrue;TestFalse;TestTrue"),
            ("TestTrue", "TestTrue; TestFalse; TestTrue"),
        ],
        "test_false": [
            (100, [200, 200]),
            ("TestTrue", ("TestFalse", "TestFalse")),
            ("TestTrue", ["TestFalse", "TestFalse"]),
            ("TestTrue", "TestFalse TestFalse"),
            ("TestTrue", "TestFalse,TestFalse"),
            ("TestTrue", "TestFalse, TestFalse"),
        ],
        "test_exception": [
            ("TestException", 100)
        ],

    },

    "NotIn": {
        "test_true": [
            (100, [200, 200]),
            ("TestTrue", ("TestFalse", "TestFalse")),
            ("TestTrue", ["TestFalse", "TestFalse"]),
            ("TestTrue", "TestFalse TestFalse"),
            ("TestTrue", "TestFalse,TestFalse"),
            ("TestTrue", "TestFalse, TestFalse"),
        ],
        "test_false": [
            (100, [100, 200]),
            ("TestTrue", ("TestTrue", "TestFalse")),
            ("TestFalse", ("TestTrue", "TestFalse")),
            ("TestTrue", ["TestTrue", "TestTrue"]),
            ("TestTrue", "TestTrue TestFalse"),
            ("TestTrue", "TestTrue,TestFalse"),
            ("TestTrue", "TestTrue, TestFalse"),
            ("TestTrue", "TestTrue;TestFalse;TestTrue"),
            ("TestTrue", "TestTrue; TestFalse; TestTrue"),
        ],
        "test_exception": [
            ("TestException", 100)
        ],
    },
}
