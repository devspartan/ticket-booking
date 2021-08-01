# Generated by Django 3.2.5 on 2021-08-01 17:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0009_auto_20210801_1643'),
    ]

    operations = [
        migrations.AddField(
            model_name='show',
            name='screen',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tickets.screen'),
        ),
        migrations.AlterField(
            model_name='seat',
            name='seat_id',
            field=models.CharField(choices=[('A1', 'A1'), ('A2', 'A2'), ('A3', 'A3'), ('A4', 'A4'), ('A5', 'A5'), ('A6', 'A6'), ('A7', 'A7'), ('A8', 'A8'), ('A9', 'A9'), ('A10', 'A10'), ('B1', 'B1'), ('B2', 'B2'), ('B3', 'B3'), ('B4', 'B4'), ('B5', 'B5'), ('B6', 'B6'), ('B7', 'B7'), ('B8', 'B8'), ('B9', 'B9'), ('B10', 'B10'), ('C1', 'C1'), ('C2', 'C2'), ('C3', 'C3'), ('C4', 'C4'), ('C5', 'C5'), ('C6', 'C6'), ('C7', 'C7'), ('C8', 'C8'), ('C9', 'C9'), ('C10', 'C10'), ('D1', 'D1'), ('D2', 'D2'), ('D3', 'D3'), ('D4', 'D4'), ('D5', 'D5'), ('D6', 'D6'), ('D7', 'D7'), ('D8', 'D8'), ('D9', 'D9'), ('D10', 'D10'), ('E1', 'E1'), ('E2', 'E2'), ('E3', 'E3'), ('E4', 'E4'), ('E5', 'E5'), ('E6', 'E6'), ('E7', 'E7'), ('E8', 'E8'), ('E9', 'E9'), ('E10', 'E10'), ('F1', 'F1'), ('F2', 'F2'), ('F3', 'F3'), ('F4', 'F4'), ('F5', 'F5'), ('F6', 'F6'), ('F7', 'F7'), ('F8', 'F8'), ('F9', 'F9'), ('F10', 'F10'), ('G1', 'G1'), ('G2', 'G2'), ('G3', 'G3'), ('G4', 'G4'), ('G5', 'G5'), ('G6', 'G6'), ('G7', 'G7'), ('G8', 'G8'), ('G9', 'G9'), ('G10', 'G10')], max_length=4),
        ),
    ]