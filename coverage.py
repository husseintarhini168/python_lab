...
    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-python@v4
        with:
          python-version: 3.11

      - name: Install dependencies
        ...

      - name: Run coverage
        run: |
          coverage run ...
          coverage report -m

      - name: Coverage Badge
        uses: tj-actions/coverage-badge-py@v2

      - name: Verify Changed files
        uses: tj-actions/verify-changed-files@v16
        id: verify-changed-files
        with:
          files: coverage.svg

      - name: Commit files
        if: steps.verify-changed-files.outputs.files_changed == 'true'
        run: |
          git config --local user.email "github-actions[bot]@users.noreply.github.com"
          git config --local user.name "github-actions[bot]"
          git add coverage.svg
          git commit -m "Updated coverage.svg"

      - name: Push changes
        if: steps.verify-changed-files.outputs.files_changed == 'true'
        uses: ad-m/github-push-action@master
        with:
          github_token: ${{ secrets.github_token }}
          branch: ${{ github.ref }}