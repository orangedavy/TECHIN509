from flask import Flask, render_template, request, redirect, url_for, flash
from logic import *

app = Flask(__name__)